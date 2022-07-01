class FoodGroupsContract:
    TABLE_NAME = "food_groups"

    class Columns:
        ID = "id"
        GROUP_NAME = "group_name"
        URL = "url"


class FoodsContract:
    TABLE_NAME = "foods"

    class Columns:
        ID = "id"
        GROUP_ID = "group_id"
        FOOD_NAME = "food_name"
        KKAL = "kkal"
        BELKI = "belki"
        FATS = "fats"
        UGL = "ugl"
        URL = "url"
