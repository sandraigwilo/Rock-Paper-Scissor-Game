class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    def change_name(self, new_name):
        self.name = new_name
        return self.name
    def change_age(self, new_age):
        self.age = new_age 
        return self.age
    def add_track(self, new_tracks):
        self.tracks.append(new_tracks)
        return self.tracks
    def get_score(self):
        return self.score        




Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)


# Expected methods
name = Bob.change_name("Peter")
age = Bob.change_age(34)
tracks = Bob.add_track("UI/UX")
score = Bob.get_score()

print("New name:", name)
print("New age:", age)
print("New tracks:", tracks)
print("Score:", score)
