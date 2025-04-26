from graph import app
import pprint

if __name__ == "__main__":
    query = "Compare the benefits and drawbacks of solar vs. wind energy in Europe."
    pprint.pprint(app.invoke(input={"query": query}))