1. What does a model's field type represent? If I use a CharField versus a TextField, for example, what does that change about how the data is stored?
    - It represents the data type meant for that field. CharField is meant for small amounts of text, such as single sentences, whereas TextField is meant for a large body of text.
2. What is the difference between the null and blank field options? What do each of them represent?
    - Null is meant for database related tasks and blank is for form validation purposes.
3. How do we use the TextChoices field type to display multiple options?
    - You created a sequence of 2-tuples to use as choices. The first argument is what is stored in the database and the second argument is what is displayed by the form's widget.
4. What is a primary_key field? If we don't specify a primary key, what is the default?
    - The primary key field is what identifies the tuple. If left unspecified, Django will automatically add an integer field.
5. How do we specify a verbose name? What purpose does it serve?
    - Each field type besides a select few have an optional first posititional argument, so the verbse name would be defined there. It serves as a way to identify the object.
6. In the documentation under "Many-to-one Relationships", an example is given of "Manufacturer" and "Car" models. Complete the code by adding at least 2 new fields to each model.
    - country = models.ForeignKey(Country, on_delete=models.CASCADE), rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    - model = models.ForeignKey(Model, on_delete=models.CASCADE), trim = models.ForeignKey(Trim, on_delete=models.CASCADE)
7. In the documentation under "Many-to-Many Relationships", an example is given of "Pizza" and "Topping" models. Complete the code by adding at least 2 new fields to each model.
    - pepperoni = models.ForeignKey(Pepperoni, on_delete=models.CASCADE), italian_sausage = models.ForeignKey("Italian Sausage", on_delete=models.CASCADE)
    - size = models.ManyToManyField(Size), sauce = models.ManyToManyField(Sauce)
8. What is an example of a one-to-one relationship? When would we use a OneToOneField?
    - An example would be an Electronics model and Laptop model, because they both contain similar information in terms of Field types. A OneToOneField would be used when you want to build on top of another database that stores similar information and is relevant to the data.
9. Sometimes we need to relate a model to one from another app. Give an example of an import line to show how we'd import the other model.
    - from geography.models import ZipCode
10. What is the class Meta? When would we use it?
    - The meta class is used for storing metadata. According to Django, Model metadata is “anything that’s not a field.”
11. What is an example of a model method? Suppose we have a class Album. What methods might we want to write for it?
    - An example would be putting formulas that help calculate taxes while the model takes care of the variable assigning, etc.. We would most likely write methods that get information such as the songs and artist(s).
12. Give an example of model inheritance. How does inheritance help us to write better code?
    - An example would be using abstract base classes where you define common information for other models. It will then be used as a base class for other models. Inheritance allows us to write less code and increase code readibility.