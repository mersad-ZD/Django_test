from django.shortcuts import render,get_object_or_404
from .models import bookshelfs


def whichFunction(request):
    removeButtonValue = request.GET.get('removeButton', False)
    saveButtonValue = request.GET.get('saveButton', False)
    editButtonValue = request.GET.get('editButton', False)
    updateButtonValue = request.GET.get('updateButton', False)

    if(len(request.GET)== 0):
        bookshelf = bookshelfs.objects

        return render(request, 'showBookShelf.html', {'bookshelfs': bookshelf})


    elif updateButtonValue == "updateClicked":
        bookshelf = bookshelfs.objects

        bookID =request.GET.get('editButton')
        editingBook = bookshelfs.objects.get(id=bookID)


        name1 = request.GET['BookName']
        publicationDate1 = request.GET['PublicationDate']
        pageNumber1 = request.GET['PageNumber']
        firstPublished1 = request.GET['FirstPublished']

        editingBook.name = name1
        editingBook.publicationDate = publicationDate1
        editingBook.pageNumber = pageNumber1
        editingBook.firstPublished = firstPublished1

        editingBook.save()
        return render(request, 'showBookShelf.html', {'bookshelfs': bookshelf, 'editingBook': editingBook})





    elif int(editButtonValue) > 0:

        bookID = editButtonValue
        editingBook = bookshelfs.objects.get(id=bookID)

        return render(request, 'editPage.html', {'editingBook': editingBook, 'editButtonValue': editButtonValue})

    elif int(removeButtonValue) < 0:
        bookshelf = bookshelfs.objects

        return render(request, 'showBookShelf.html', {'bookshelfs': bookshelf})



    elif int(removeButtonValue) > 0 :
       # shelf_ID = request.GET['removeButton']
         shelf_ID = request.GET.get('removeButton')
         bookshelfs.objects.filter(id=shelf_ID).delete()

         bookshelf = bookshelfs.objects
         return render(request, 'showBookShelf.html', {'bookshelfs': bookshelf})

    elif saveButtonValue == "saveClicked":

        name1 = request.GET['BookName']
        publicationDate1 = request.GET['PublicationDate']
        pageNumber1 = request.GET['PageNumber']
        firstPublished1 = request.GET['FirstPublished']

        newBookShelf = bookshelfs(name=name1, publicationDate=publicationDate1, pageNumber=pageNumber1,
                                  firstPublished=firstPublished1)
        newBookShelf.save()
        bookshelf = bookshelfs.objects
        return render(request, 'showBookShelf.html', {'bookshelfs': bookshelf})


def edit(request):
    editButtonValue = request.GET.get('editButton', False)

    bookshelf = bookshelfs.objects
    return render(request, 'editPage.html', {'bookshelfs': bookshelf, 'editButtonValue': editButtonValue})
