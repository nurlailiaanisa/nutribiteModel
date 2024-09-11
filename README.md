# Rekomendasi Resep Berdasarkan KNN dan TF-IDF

Proyek ini menggunakan teknik *Natural Language Processing* (NLP) dan *Machine Learning* untuk merekomendasikan resep makanan yang mirip dengan resep yang disukai pengguna. Model K-Nearest Neighbors (KNN) dan TF-IDF digunakan untuk menemukan resep yang paling relevan.

## Daftar Isi
- [Pendahuluan](#pendahuluan)
- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Penggunaan](#penggunaan)
- [Lisensi](#lisensi)

## Pendahuluan

Proyek ini bertujuan untuk memberikan rekomendasi resep makanan kepada pengguna berdasarkan resep yang mereka sukai. Dengan memanfaatkan TF-IDF untuk mengubah teks resep menjadi vektor dan model KNN untuk mencari kemiripan antar resep, proyek ini dapat menemukan resep yang mirip dan sesuai dengan preferensi pengguna.

## Fitur

- Memuat dan memproses dataset resep makanan.
- Mengubah teks resep menjadi representasi vektor menggunakan TF-IDF.
- Melatih model KNN untuk mencari resep yang mirip.
- Memberikan rekomendasi resep berdasarkan input pengguna.

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan proyek ini di lingkungan lokal Anda:

1. **Clone repositori ini:**

   ```bash
   git clone https://github.com/nurlailiaanisa/nutribiteModel.git
   cd nutribiteModel/app

2. **Buat environment virtual dan aktifkan::**
   ```bash
   python -m venv env
   source env/bin/activate   # Untuk pengguna Unix/macOS
   .\env\Scripts\activate    # Untuk pengguna Windows

3. **Instalasi Library:**
   ```bash
   pip install requirements.txt

## Penggunaan

1. **Jalankan model app.py:**

   Jika anda tidak memiliki URL Endpoint, dapat menggunakan Flask API untuk memperoleh URL lokal seperti ```http://127.0.0.1:5000``` atau ```http://localhost:5000```
    ```bash
    python app.py

2. **Uji model dan dapatkan rekomendasi:**
   
   Kirimkan request JSON menggunakan tool seperti Postman atau cURL. Berikut adalah contoh request JSON:
```bash
{
    "calories":2000,
    "liked_recipes":
    [
        {
            "calories": 497.2,
            "carbo": 84.3,
            "cook_min": 25.0,
            "directions": "Mix all of the ingredients together in a sauce pan. Set on stove until it begins to boil. Turn heat to low. Cover and cook until rice is done and the water is absorbed. Removed bay leaves and lemon grass before serving.",
            "intro": "An Indonesian fragrant rice dish cooked with coconut milk and turmeric",
            "prep_min": 5.0,
            "protein": 8.5,
            "recipe_title": "Nasi Kuning",
            "servings": 4,
            "total_fat": 13.8,
            "yield_unit": "4 servings"
        },
        {
            "calories": 484.0,
            "carbo": 19.0,
            "cook_min": 10.0,
            "directions": "Whisk together brown sugar, fish sauce, garlic, onion, oil, soy sauce, coriander, ginger, cumin, turmeric, and cayenne pepper in a mixing bowl until smooth.  Bruise lemongrass by hitting it lightly several times with the back of a large chef's knife; mince lemongrass and add to marinade.  Cut beef sirloin into strips about 2 1/2-inches long and 1/8 inch-thick. Stir beef into marinade until beef is completely coated, about 1 minute. Cover the bowl with plastic wrap and marinate in the refrigerator for 2 to 4 hours.  Preheat an outdoor grill for high heat. Lightly oil the grate.  Remove beef from marinade and shake off excess marinade. Thread 1/4 of the meat onto each metal skewer. Discard remaining marinade.  Arrange skewers on the preheated grill; cook until meat stops sticking to the grill, 1 to 2 minutes. Flip skewers and continue cooking until meat is well browned and shows grill marks, 2 to 2 1/2 minutes. Flip skewers once more; cook until meat is still slightly pink, about 2 minutes. Transfer skewers to a platter; let rest for 2 minutes before serving.",
            "intro": "This beef satay recipe is the main course-size version of a fabulous Thai appetizer: strips of beef marinated in Asian spices, skewered, and grilled for a truly amazing combination of flavors. With grilling season still in full swing, you can never have enough new and exciting ways to enjoy beef. Serve with my peanut dipping sauce.",
            "prep_min": 15.0,
            "protein": 40.0,
            "recipe_title": "Beef Satay",
            "servings": 4,
            "total_fat": 27.0,
            "yield_unit": "4 skewers"
        },
        {
            "calories": 292.11,
            "carbo": 35.64,
            "cook_min": 0.0,
            "directions": "Combine all ingredients; toss gently to mix.  Taste and add lemon juice if desired.  Chill until ready to serve.",
            "intro": "NaN",
            "prep_min": 15.0,
            "protein": 10.98,
            "recipe_title": "White Bean, Olive and Tomato Salad",
            "servings": 4,
            "total_fat": 11.74,
            "yield_unit": "4 cups"
        },
        {
            "calories": 178.12,
            "carbo": 32.4,
            "cook_min": 10.0,
            "directions": " Cook rotini twists according to package directions.  Drain and rinse in cold water; drain well.  In a large mixing bowl, combine cooked rotini, cherries, cucumber, carrot and onion; mix well.  In a small bowl, combine salad dressing.  lemon juice, dill and black pepper.  Pour dressing over pasta mixture, tossing to coat.  Cover and refrigerate 1 to 2 hours, or overnight. ",
            "intro": "Perfect for a potluck or family get-together.",
            "prep_min": 10.0,
            "protein": 4.65,
            "recipe_title": "Cheery Cherry Pasta Salad",
            "servings": 8,
            "total_fat": 3.32,
            "yield_unit": "5 cups"
        }
    ]
}
   ```
   atau bisa juga menggunakan contoh request JSON seperti ini yg penting terdapat key directions:
   ```bash
{
   "calories": 2000,
   "liked_recipes": 
   [
      {"directions": "Mix all of the ingredients together in a sauce pan. Set on stove until it begins to boil. Turn heat to low. Cover and cook until rice is done and the water is absorbed. Removed bay leaves and lemon grass before serving."},
      {"directions": "Whisk together brown sugar, fish sauce, garlic, onion, oil, soy sauce, coriander, ginger, cumin, turmeric, and cayenne pepper in a mixing bowl until smooth.  Bruise lemongrass by hitting it lightly several times with the back of a large chef's knife; mince lemongrass and add to marinade.  Cut beef sirloin into strips about 2 1/2-inches long and 1/8 inch-thick. Stir beef into marinade until beef is completely coated, about 1 minute. Cover the bowl with plastic wrap and marinate in the refrigerator for 2 to 4 hours.  Preheat an outdoor grill for high heat. Lightly oil the grate.  Remove beef from marinade and shake off excess marinade. Thread 1/4 of the meat onto each metal skewer. Discard remaining marinade.  Arrange skewers on the preheated grill; cook until meat stops sticking to the grill, 1 to 2 minutes. Flip skewers and continue cooking until meat is well browned and shows grill marks, 2 to 2 1/2 minutes. Flip skewers once more; cook until meat is still slightly pink, about 2 minutes. Transfer skewers to a platter; let rest for 2 minutes before serving."},
      {"directions": "Cook rotini twists according to package directions.  Drain and rinse in cold water; drain well.  In a large mixing bowl, combine cooked rotini, cherries, cucumber, carrot and onion; mix well.  In a small bowl, combine salad dressing.  lemon juice, dill and black pepper.  Pour dressing over pasta mixture, tossing to coat.  Cover and refrigerate 1 to 2 hours, or overnight."},
      {"directions": "Combine beans, corn, celery onion, pimiento, and green pepper.  Moisten to taste with Golden Gate Dressing.  Chill.\n\nGolden Gate Dressing:  Mix dry ingredients:  sugar, dry mustard, salt, flour.  Beat egg with fork in small bowl.  Beat in dry mixture.  Heat vinegar, water and butter in saucepan.  Remove from heat while you gradually add egg mixture, stirring fast.  Then put back to cook, stirring constantly, 2 or 3 minutes, until smooth and thick.  Makes 1-3/4 cups.  Fine for potato, cabbage, tuna or other salads.\n\nNote:  2 egg yolks may be used instead of 1 whole egg."},
      {"directions": "Rub pears with lemon juice to prevent browning.  Place pear halves, cut side down, on steamer rack.  Steam pears 4 to 5 minutes or until tender when pierced with knife tip.  Cool to room temperature; refrigerate to chill.  Puree raspberries in blender or food processor; press through sieve to remove seeds.  Stir sugar into yogurt.  Place yogurt in pastry bag fitted with fine tip or in plastic squeeze-type mustard or ketchup bottle.  Pour about 1/4 cup raspberry puree on each of 4 dessert plates.  Pipe yogurt in spiral design on sauce.  Draw knife from center of plate, spoke-fashion, to create web design.  Place chilled pear half, cut side down, on sauce.  Arrange orange zest on pear.  Garnish plates with mint, if desired."}
   ]
}
   ```

3. **Contoh Menggunakan Postman**

   - Pilih metode POST dan URL endpoint (```(URL Endpoint)/predict```).
   - Di tab "Body", pilih "raw" dan pastikan formatnya adalah "JSON".
   - Masukkan JSON seperti contoh di atas.
   - Kirim permintaan dan lihat hasil rekomendasi.

## Lisensi
- IMT
-
