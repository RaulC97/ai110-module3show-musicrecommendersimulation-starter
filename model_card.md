# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
    - **SongFlexx**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
    - Recommends different songs based on favorite genre, mood, and other features
- What assumptions does it make about the user  
    - They have a favorite common genre
- Is this for real users or classroom exploration  
    - classroom exploration

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
    - genre,mood,energy,tempo_bpm,valence,danceability,acousticness
- What user preferences are considered  
    - Genre and mood
- How does the model turn those into a score  
    - each feature has different weights, with genre, mood, and energy being the highest
- What changes did you make from the starter logic  
    - added more songs for greater

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
    - there are 20 songs total
- What genres or moods are represented  
    - Common ones: pop, lofi, rock and less than common: country, edm, blues
- Did you add or remove data  
    - Added 10 extra songs from starter code.
- Are there parts of musical taste missing in the dataset  
    - theres still quite a bit of genres not represented, and my stress test users
    show, such as a trap music user.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
    - pop, lofi seemed to get the best results.
- Any patterns you think your scoring captures correctly  
    - having genre, mood, and energy having high weights.
- Cases where the recommendations matched your intuition  
    - I think pop and lofi got the most.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
    - some features like tempo dont need to be included by user
- Genres or moods that are underrepresented  
    - Folk, and Blues
- Cases where the system overfits to one preference  
    - lofi I believe
- Ways the scoring might unintentionally favor some users  
    - if there favorite genre is very common.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
    - Pop, lofi, rock, and sab but high energy, trap, and classical but fast
- What you looked for in the recommendations  
    - genre and mood matching
- What surprised you  
    - how it chooses genres that aren't part of the dataset
- Any simple tests or comparisons you ran  
    - ran users that seemed contradictory to test how well it would match

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
    - song length, decade prefrence
- Better ways to explain recommendations 
    - visualization on how songs are ranked/picked
- Improving diversity among the top results  
    - adding more data
- Handling more complex user tastes  
    - maybe changing the weights if user is contradictory

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
    - How smaller recommender systems like this song can be made small dataset.
- Something unexpected or interesting you discovered  
    - how accurate recommender can be even when theres a smaller dataset
- How this changed the way you think about music recommendation apps  
    - thinking how newer songs can affect a users perfrences.
