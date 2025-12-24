class Content:

    def __init__(self, content_name, contentCreator, genre):
        self.content_name= content_name
        self.contentCreator= contentCreator
        self.genre= genre
        self.number_of_views= 0
        self.listOfRatings= [] #רשימת דירוגים (מספרים)

    def add_view(self):
        self.number_of_views+= 1

    def add_rating(self, rating):
        if 0 <= rating <= 5:
            self.listOfRatings.append(rating)
            return True
        return False

    def get_average_rating(self):
        return sum(self.listOfRatings) / len(self.listOfRatings)

    def set_genre(self, genre):
        allowed_genres= ["Action", "Comedy", "Drama", "Science"]
        if genre in allowed_genres:
            self.genre= genre
            return True
        print("Genre not allowed")
        return False

    def print_details(self):
        print(f"Content name: {self.content_name}")
        print(f"Genre: {self.genre}")
        print(f"Number of views: {self.number_of_views}")

class Viewer:

    def __init__(self, user_id, user_name):
        self.user_id= user_id
        self.user_name= user_name
        self.listOfViewed= [] #רשימת תכנים שצפה
        self.listOfRated= [] #רשימת תכנים שדירג

    def watch_content(self, content: Content):
        if content in self.listOfViewed:
            return False
        content.add_view()
        self.listOfViewed.append(content)
        return True

    def rate_content(self, content: Content, rating):
        if content in self.listOfRated:
            return False
        if content.add_rating(rating):
            self.listOfRated.append(content)
            return True
        return False

    def print_details(self):
        print(f"Name: {self.user_name}")
        print("Content Watched:")
        for content in self.listOfViewed:
            print(content.content_name)
        print("Content Rated:")
        for content in self.listOfViewed:
            print(f"{content.content_name} Rating: {content.get_average_rating()}")

class Creator(Viewer):

    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
        self.listOfUploads= []

    def upload_content(self, content: Content):
        if content in self.listOfUploads:
            return False
        if len(self.listOfUploads) >= 10:
            return False
        self.listOfUploads.append(content)
        return True

    def print_details(self):
        print(f"Name: {self.user_name}")
        print("Content Uploaded:")
        for content in self.listOfUploads:
            print(content.content_name)

class PlatformManager(Viewer):

    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
        self.listOfCreators= []
        self.listOfUploads = []

    def upload_content(self, content: Content):
        if content in self.listOfUploads:
            return False
        if len(self.listOfUploads) >= 20:
            return False
        self.listOfUploads.append(content)
        return True

    def add_creator(self, creator: Creator):
        if creator in self.listOfCreators:
            return False
        self.listOfCreators.append(creator)
        return True

    def print_details(self):
        print(f"Name: {self.user_name}")
        print("Creators Under Manager:")
        for creator in self.listOfCreators:
            print(creator.user_name)


co1= Content("Epic Movie", "Alice", "Action")
co2= Content("Funny Show", "Bob", "Comedy")
v1= Viewer(1, "David")
v2= Viewer(2, "May")
cr1= Creator(3, "Michael")
cr2= Creator(4, "Loli")
m= PlatformManager(5, "Anatoli")
cr1.upload_content(co1)
cr2.upload_content(co2)
v1.watch_content(co1)
co2.add_view()
co2.add_view()
co2.add_view()
co1.add_view()
v1.rate_content(co1, 4.5)
v2.watch_content(co2)
v2.rate_content(co2, 5)
m.add_creator(cr1)
m.add_creator(cr2)
co1.print_details()
co2.print_details()
cr1.print_details()
cr2.print_details()
m.print_details()
co2.add_view()
co2.add_view()
co2.add_view()
co1.add_view()