
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django_q.tasks import async_task
from django.core.files.storage import default_storage
import textract # You may need to install this module
from .models import Activity
from .ai_functions import ai_assistant

import requests
from bs4 import BeautifulSoup
import os
import PyPDF2

def hook_funcs(task):
    print("Openai Answer are done..!")


@receiver(post_save, sender=Activity)
def activity_saved(sender, instance, **kwargs):
    
    print("signals-=------!")
    
    # Use the "created" flag to check if the instance was just created        
    if instance.file and kwargs.get('created'):
        # Get the file path from the storage
        file_path = default_storage.path(instance.file.name)

        # Determine the file extension
        _, file_extension = os.path.splitext(file_path)

        # Extract the text from the file based on the file type
        if file_extension.lower() == '.pdf':
            # Extract text from PDF using PyPDF2 with PdfReader
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for page_number in range(len(reader.pages)):
                    text += reader.pages[page_number].extract_text()
        else:
            # Extract text from other text-based files using textract
            text = textract.process(file_path).decode()

        # Update the content field with the extracted text
        instance.content = text

        # Save the instance again
        instance.save()
    elif instance.url and kwargs.get('created'):
        # Make a request to the url and get the HTML content
        response = requests.get(instance.url)
        html = response.text

        # Create a Beautiful Soup object from the HTML content
        soup = BeautifulSoup(html, 'html.parser')

        # Define the allowed tags that usually contain text content
        allowed_tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote']

        # Extract the text content from the allowed tags
        text_elements = soup.find_all(allowed_tags)

        # Use stripped_strings generator to remove any extra tags within the allowed tags
        text = [' '.join(element.stripped_strings) for element in text_elements]

        # Save the text content to the description field of the instance
        instance.content = ' '.join(text)

        # Save the instance again without sending a signal to avoid recursion
        instance.save()


        
        # ai_assistant(instance)
    if instance.run_gpt:
        async_task(ai_assistant, instance, hook=hook_funcs)
