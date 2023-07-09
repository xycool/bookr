from django.contrib import admin

from reviews.models import (Book, Publisher, Contributor, BookContributor, Review)

def initialled_name(obj):
    """ obj.first_names='Jerome David', obj.last_names='Salinger'
        => 'Salinger, JD' """
    initials = ''.join([name[0] for name in \
                        obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)

class ContributorAdmin(admin.ModelAdmin):
    # list_display = (initialled_name,)
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')    

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn', 'publisher__name')
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher','publication_date')

    def isbn13(self, obj):
        """ '9780316769174' => '978-0-31-676917-4' """
        return "{}-{}-{}-{}-{}".format\
                                (obj.isbn[0:3], obj.isbn[3:4],\
                                 obj.isbn[4:6], obj.isbn[6:12],\
                                 obj.isbn[12:13])

class ReviewAdmin(admin.ModelAdmin):
    # exclude = ('date_edited',)
    #fields = ('content', 'rating', 'creator', 'book')
    fieldsets = ((None, {'fields': ('createor', 'book')}), 
                 ('Review content', {'fields': ('content', 'rating')}))


# Register your models here.
#

admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
