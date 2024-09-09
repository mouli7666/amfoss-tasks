# Thisis the code for telegram bot


import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import asyncio
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build


logging.basicConfig(level=logging.INFO)


TOKEN = '7386063755:AAGrBYUha5yrsWV8bia2KrwatXtmwGPiGnQ'


GOOGLE_BOOKS_API_KEY = 'AIzaSyBDbw9nFKPJpLU-cDiLxvIvAEHFl0DKOOk'


books_service = build('books', 'v1', developerKey=GOOGLE_BOOKS_API_KEY)


last_search_results = {}
user_reading_lists = {}

async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to Chandra\'s Books! ')

async def books(update, context):
    query = ' '.join(context.args)
    print(f"Query: {query}")  

    if not query:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Please provide a book title or author! '
        )
        return

    try:
        response = books_service.volumes().list(q=query).execute()
        print(f"Response: {response}")  # Log the API response
        volumes = response.get('items', [])

        if volumes:
            book_links = []
            last_search_results[update.effective_chat.id] = volumes
            for volume in volumes:
                title = volume["volumeInfo"].get("title", "No Title")
                info_link = volume["volumeInfo"].get("infoLink", "#")
                book_links.append(f'<a href="{info_link}">{title}</a>')
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='\n'.join(book_links),
                parse_mode='HTML'
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='No books found! '
            )
    except HttpError as e:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'Error: {e.resp.status} {e.resp.reason}'
        )


async def preview(update, context):
    query = ' '.join(context.args)
    if query:
        try:
            response = books_service.volumes().list(q=query).execute()
            volumes = response.get('items', [])
            if volumes:
                preview_link = volumes[0]["volumeInfo"]["previewLink"]
                await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Preview: {preview_link}')
            else:
                await context.bot.send_message(chat_id=update.effective_chat.id, text='No books found! ')
        except HttpError as e:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Error: {e.resp.status} {e.resp.reason}')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Please provide a book title or author! ')

async def list_books(update, context):
    chat_id = update.effective_chat.id
    books = last_search_results.get(chat_id, [])

    if books:
        message = "Here are your last searched books:\n"
        for i, book in enumerate(books, 1):
            message += f"{i}. {book['volumeInfo']['title']} by {', '.join(book['volumeInfo'].get('authors', ['Unknown author']))}\n"
            message += f"   Published by {book['volumeInfo'].get('publisher', 'Unknown publisher')} on {book['volumeInfo'].get('publishedDate', 'Unknown date')}\n"
            message += f"   Preview: {book['volumeInfo'].get('infoLink', 'No link available')}\n\n"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="You haven't searched for any books yet.")

async def add_to_reading_list(update, context):
    if len(context.args) != 1:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Usage: /add <book number>")
        return

    try:
        book_number = int(context.args[0]) - 1  # Convert to zero-based index
        chat_id = update.effective_chat.id
        books = last_search_results.get(chat_id, [])

        if 0 <= book_number < len(books):
            book = books[book_number]['volumeInfo']
            reading_list = user_reading_lists.get(chat_id, [])
            reading_list.append(book)
            user_reading_lists[chat_id] = reading_list
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Added '{book['title']}' to your reading list.")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid book number. Please enter a valid number from the list.")
    except ValueError:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide a valid number.")

async def reading_list(update, context):
    reading_list = user_reading_lists.get(update.effective_chat.id, [])
    if reading_list:
        message = "Your Reading List:\n"
        for book in reading_list:
            message += f"{book['title']} by {', '.join(book.get('authors', ['Unknown author']))}\n"
            message += f"Preview: {book.get('infoLink', 'No link available')}\n\n"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Your reading list is empty.')

async def help_command(update, context):
    help_text = (
        "/start - Welcome message\n"
        "/books - Search for books by title or author\n"
        "/preview - Get a preview link for a specific book\n"
        "/list - List your last searched books\n"
        "/add - Add a book to your reading list\n"
        "/readinglist - Show your reading list\n"
        "/help - Show this help message"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("books", books))
    application.add_handler(CommandHandler("preview", preview))
    application.add_handler(CommandHandler("list", list_books))
    application.add_handler(CommandHandler("add", add_to_reading_list))
    application.add_handler(CommandHandler("readinglist", reading_list))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling()

if __name__ == '__main__':
    main()

