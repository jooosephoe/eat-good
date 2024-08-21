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

> Some charts will be shown regarding how much of the macro/micro nutrients have been eaten that day, and how much of the recommended daily intake (RDI) have been fulfilled

### Database

users: id integer PK, public_id string(50), name string(50), password string(80), height integer, weight integer, age integer, gender string(1), activity_level string(1), admin boolean

> public_id will be hex-generated uuid, gender will be m or f, activity level will be s (sedentary) or l (light exercise 1-2x/week) or m (moderate exercise 3-5x/week) or h (heavy exercise 7x/week) or a (athlete 2x/day)

user_health: id integer PK, user_id integer FK ref users.id, tdee integer, calorie_goal string(1), dietary_pref string(20)

> tdee will be the number of calories, calorie_goal will be either c (cut) or m (maintenance) or b (bulk), dietary_pref will be describing dietary preferences such as vegan, vegetarian, etc.

allergies: id integer, user_id integer FK ref users.id, allergy String(25)

cart: id integer, user_id integer FK ref users.id

cart_item: id integer, cart_id integer FK ref cart.id, item string(50)

tracker: id integer, user_id integer FK ref users.id

tracker_item: id integer, tracker_id integer FK ref tracker.id, item string(50), meal string(1), serving_type string(2), serving_amount integer

> meal will be b (breakfast) or l (lunch) or d (dinner) or s (snack), serving_type will describe unit either g (grams) or ml (mililitres) etc, serving_amount will be the number for that unit