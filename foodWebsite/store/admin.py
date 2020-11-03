from django.contrib import admin
from .models import Beverages, Groceries, HoisinSauce, Desserts, Chipsandfries, Fats, Meals, Meats, Freshfoods, \
    Fruitjuices, Fishandmeatandeggs, Sandwiches, Spreads, Parve, Pickles


class PicklesMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class ParveMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class SpreadsMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class SandwichesMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class FishandmeatandeggsMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class FruitjuicesMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class FreshFoodMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class MeatsMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class MealsMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class FatsMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class ChipsandfriesMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class DessertsMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class BeveragesMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class GroceriesMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


class HoisinSauceMeta(admin.ModelAdmin):
    list_display = (
        'product_name', 'main_category', 'main_category_en', 'image_url', 'energy', 'energy_from_fat', 'fat',
        'saturated_fat', 'butyric_acid', 'caproic_acid', 'caprylic_acid', 'capric_acid', 'lauric_acid', 'myristic_acid',
        'palmitic_acid', 'stearic_acid', 'arachidic_acid', 'behenic_acid', 'lignoceric_acid', 'cerotic_acid',
        'montanic_acid', 'melissic_acid', 'monounsaturated_fat', 'polyunsaturated_fat', 'omega_3_fat',
        'alpha_linolenic_acid', 'eicosapentaenoic_acid', 'docosahexaenoic_acid', 'omega_6_fat', 'linoleic_acid',
        'arachidonic_acid', 'gamma_linolenic_acid', 'dihomo_gamma_linolenic_acid', 'omega_9_fat', 'oleic_acid',
        'elaidic_acid', 'gondoic_acid', 'mead_acid', 'erucic_acid', 'nervonic_acid', 'trans_fat', 'cholesterol',
        'carbohydrates', 'sugars', 'sucrose', 'glucose', 'fructose', 'lactose', 'maltose', 'maltodextrins', 'starch',
        'polyols', 'fiber', 'proteins', 'casein', 'serum_proteins', 'nucleotides', 'salt', 'sodium', 'alcohol',
        'vitamin_a', 'beta_carotene', 'vitamin_d', 'vitamin_e', 'vitamin_k', 'vitamin_c', 'vitamin_b1', 'vitamin_b2',
        'vitamin_pp', 'vitamin_b6', 'vitamin_b9', 'folates', 'vitamin_b12', 'biotin', 'pantothenic_acid', 'silica',
        'bicarbonate', 'potassium', 'chloride', 'calcium', 'phosphorus', 'iron', 'magnesium', 'zinc', 'copper',
        'manganese', 'fluoride', 'selenium', 'chromium', 'molybdenum', 'iodine', 'caffeine', 'taurine', 'ph',
        'fruits_vegetables_nuts', 'fruits_vegetables_nuts_estimate', 'collagen_meat_protein_ratio', 'cocoa',
        'chlorophyl',
        'carbon_footprint', 'nutrition_score_fr', 'nutrition_score_uk', 'glycemic_index', 'water_hardness')


admin.site.register(Beverages, BeveragesMeta)
admin.site.register(Groceries, GroceriesMeta)
admin.site.register(HoisinSauce, HoisinSauceMeta)
admin.site.register(Chipsandfries, DessertsMeta)
admin.site.register(Fats, FatsMeta)
admin.site.register(Meals, MealsMeta)
admin.site.register(Meats, MeatsMeta)
admin.site.register(Freshfoods, FreshFoodMeta)
admin.site.register(Fruitjuices, FruitjuicesMeta)
admin.site.register(Fishandmeatandeggs, FishandmeatandeggsMeta)
admin.site.register(Sandwiches, SandwichesMeta)
admin.site.register(Spreads, SpreadsMeta)
admin.site.register(Parve, ParveMeta)
admin.site.register(Pickles, PicklesMeta)
