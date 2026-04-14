# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
    - My system uses genre, mood, valence, energy, danceability and acousticness. Genre and Mood have higher weights making up .65 , while danceability and acousticness have lower weights
- What information does your `UserProfile` store
  - Currently UserProfile stores favorites in genre, mood, energy, and liking acoustic.
- How does your `Recommender` compute a score for each song
  - Current Recommender will set the weights for as follows: .35 genre, .30 mood, .12 valence, .10 energy, .08 danceability, .05 acousticness.
- How do you choose which songs to recommend
  - Large based on genre and mood. If the genre and or mood is a match, chances are the song is a match to the
  user.

You can include a simple diagram or bullet list if helpful.

<img width="1693" height="822" alt="Screenshot 2026-04-13 205019" src="https://github.com/user-attachments/assets/859050d2-4d73-4cec-81f1-79bcf9f06c0e" />


<img width="406" height="681" alt="Screenshot 2026-04-13 210444" src="https://github.com/user-attachments/assets/606f5673-8e36-4bfa-8d8a-361d3542ad9e" />

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
  - the recommendation were worse
- What happened when you added tempo or valence to the score
  - It gave slight increases, but I dont think i had enough data to make it have be a difference
- How did your system behave for different types of users
  - worked well

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:


- It doesn't work too well if genres that aren't in the dataset

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:


- In this music recommender, it takes a users prefrences in genre, mood, energy etc,
and plugs it into a system that ranks what songs it you will like.


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> SongFlexx

---

## 2. Intended Use

- What is this system trying to do
- Who is it for


the model suggests 5 songs from a 20 songs catalog based on users prefrred genre, mood,etc. Used for classroom setting. 

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
  - genre,mood,energy,tempo_bpm,valence,danceability,acousticness
- What information about the user does it use
  - Genres and mood have major weights, while the others lesser weights
- How does it turn those into a number
  - each features 

Try to avoid code in this section, treat it like an explanation to a non programmer.



---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
  - 20 songs
- Did you add or remove any songs
  - added 10 songs from starter code
- What kinds of genres or moods are represented
  - Common ones: pop, lofi, rock and less than common: country, edm, blues
- Whose taste does this data mostly reflect
  - mosrtly pop and lofi

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
  - pop, lofi
- Particular user profiles it served well
  - pop, lofi, rock
- Simplicity or transparency benefits
  - simplicity

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
  - yes the less common ones, country, edm, and blues
- Does it treat all users as if they have the same taste shape
  - no
- Is it biased toward high energy or one genre by default
  - No
- How could this be unfair if used in a real product
  - would give more popular genre and moods versus lesser ones

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
  - Yes multiple users
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
  - no
- You wrote tests for your scoring logic
  - yes

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- I would want to add more songs if different genres and moods to give more data sample to be more fair.

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
  - How well the recommender be with low ammount of data points there
- How did building this change how you think about real music recommenders
  - how accurate recommender can be even when theres a smaller dataset
- Where do you think human judgment still matters, even if the model seems "smart"
  - I think mood would be a hard to put in a model, because i feel like you can categories mood into sub categories.

