import json
#Create Like counting class
class LikeDB:
    def __init__(self, db_path):
        #Initialize the database
        #Open the database file if it exists, otherwise create a new database file
        self.db_path = db_path
        try:
            with open(db_path, 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {}
            #Save the database to the database file
            with open(db_path, 'w') as f:
                json.dump(self.db, f, indent=4)

    def save(self):
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=4)
    
    def all_likes(self):
        """Counts all users likes
        returns
            all users likes
        """
        likes = 0
        if self.db:
            for usier, v in self.db.items():
                likes += v['likes']
        
        return likes
        
    def all_dislikes(self):
        """Counts all users dislikes
        returns
            all users dislikes
        """
        likes = 0
        if self.db:
            for usier, v in self.db.items():
                likes += v['dislikes']
        
        return likes
        
        
        
    #Add a like to the database
    def add_like(self, user_id:str)->dict:
        '''
        Add a like to the database
        args:
            user_id: The user id of the user who liked the post
        returns:
            The number of likes and dislikes for the post
        '''
        pass

  
    #Add a dislike to the database
    def add_dislike(self, user_id:str)->dict:
        '''
        Add a dislike to the database
        args:
            user_id: The user id of the user who disliked the post
        returns:
            The number of likes and dislikes for the post
        '''
        pass
x=LikeDB(db_path='like_db.json')

print(x.all_likes())