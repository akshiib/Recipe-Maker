# Recipe Maker
### Description
This project provides an interactive tool for generating recipes based on the ingredients you have at home. It leverages the Spoonacular API to fetch recipe ideas and the OpenAI API to generate detailed recipes. The recipes are then stored in a SQLite database for easy retrieval and management.

### Features
###### Ingredient Input:
Users can input the ingredients they have available in their fridge.
###### Recipe Fetching:
The app uses the Spoonacular API to fetch 3 recipe ideas based on the provided ingredients.
###### Recipe Generation:
With the help of OpenAI's GPT 4, the app generates detailed recipes from the fetched ideas.
###### Markdown Export:
Generated recipes are saved in a Markdown file (Recipe.md) for easy viewing and sharing.
###### Database Storage:
Recipes are stored in a SQLite database, recipes.db allowing users to manage and retrieve them later.
### Installation
###### Clone the repository:
```
git clone https://github.com/yourusername/recipe-maker.git
cd recipe-maker
```

###### Install the required dependencies:
```
pip install -r requirements.txt
```

###### Set up your environment variables for the API keys:
```
export API_KEY_FOOD='your_spoonacular_api_key'
export OPENAI_API_KEY='your_openai_api_key'
```

###### Usage
Run the main script:
```
python recipe_maker.py
```

Follow the prompts to input the number of ingredients and the ingredients themselves.
The app will fetch recipe ideas, generate detailed recipes, and save them both as a Markdown file and in a SQLite database.

###### Requirements
Python 3.7+
Requests
SQLite3
OpenAI Python Client
Spoonacular API Key
OpenAI API Key
Testing
This project uses automated testing and style checks via GitHub workflows. The workflows are defined in the .github/workflows directory.