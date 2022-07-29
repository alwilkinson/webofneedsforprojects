from Project_Class import Project as pr
import pandas as pd

website = pr(1, "Website", ["JS", "C"])
church_plant = pr(2, "Church Planting", ["Evangelism"])
book = pr(3, "Children's Storybook", ["Creative Writing"])

data = [website, church_plant, book]
dataframe = pd.DataFrame({"Project_ID": [pr.get_id(project) for project in data], "Title": [pr.get_title(project) for project in data], "Tags":[pr.get_tags(project) for project in data]})

def get_projects():
    print("Function not created")

def create_project():
    print("Function not created")

def remove_project():
    print("Function not created")
