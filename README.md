# eat-good
An app that allows users to get information about the food they are eating and provides better suggestions

## Plan
### Flow of App
User opens the app

-->

**either**

(Route A)
User can input a type of food -> See nutrition details, ingredients list -> Receive suggestions using AI -> Get star ratings for the food from grocery apis
> Nutrition includes macronutrients (calories, protein, carbohydrates, fat, etc.) and micro nutrients (calcium, zinc, different vitamins, etc.)
> Application will judge whether the food is healthy based on ingredients list (if there are a lot of chemicals, ingredients are natural or not, etc.)
> Suggestions will include a description of the food, better alternatives if it is not healthy, what the use case of the food is (is it a pre-workout snack? Is it a high protein snack for after workouts? Is it for a meal?)

**or**

(Route B)
User creates a profile -> Go to route A -> App will create additional judgements
> Profiles can be created and will consist of personal information (will calculate TDEE, and make suggestions based on that), dietary preferences, goals (whether they want to bulk, maintain or cut) and allergies
> Additional judgements include if the food contains any allergies and so whether or not they should eat it, calculate the calorie to protein ratio and see if it is a good 'bang for your buck' case, fits in dietary preferences, and judge if it is a fitting food for bulk, cut, or maintain

-->

**if chose Route B**

**either**

User can add food to "cart" -> When opening cart app will show where they can get it (stores and prices)

**or**

User can add to daily tracker of what they eat
> Will be able to put the serving amount and if it was for breakfast, lunch, dinner or snack

### Database

User {
    id integer PK,
    public_id string UNIQUE,
    name string,
    age integer,
    height integer,
    weight integer,
    admin boolean
}

UserPreferences {
    user_id integer PK FK,
    goals char,
    dietary_preferences string
}

Allergies {
    id integer PK,
    user_id integer FK,
    allergy string
}

Cart {

}

DailyExpenditure {

}