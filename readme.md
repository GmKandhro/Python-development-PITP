

## Day 2 Tasks – Python
## ============================

## 1. Ali bought 3 pens, he invested 10 rs for each pen. He gave the shopkeeper a note of 50, how much  he should  get back.

```python
 pens = 3
 totalRs = 3*10
 print("ALi should get " , 50 - totalRs , " back")
```



## 2.Salman has 15 chocolates he distributed them among 5 students equally, how much  he would gave a chocolate to one student. And what amount of chocolate will be left if there would only 7 students

``` python
chocolates = 15
students = 5


print("From Salman's chocolates each student will get " , chocolates / students)
print("if there would only 7 students The amount of remaning chocolates is " , chocolates % 7)
```

## 3.ALi bought 15 mangoes. then his friend gave him 7 baskets of 2 mangoes each.
### how many mangoes does ALi have in total?
``` python
baskets = 7
Ali_bought_mandoes = 15

print("Ali will have ", 2*baskets+ Ali_bought_mandoes , " mangoes")
```

## 4.A group  of students collected 20 pens.  they gave away 5 pens, and then distribute the rest equally among 3 friends
### how many pens did each friend get?
``` python
Total_pens = 20 
give_away_pens = 5

remaining_pens = Total_pens - give_away_pens

print("each friend get " , remaining_pens / 3)
```
## 5. A machine doubles its output every hour. if it produces 2 items in the first hour,
### how many will  it produce after 4 hours?

``` python
hours = 4
items = 2

print(f"The machine will Produce {items**hours } items in {hours} hours")
```
## ==========================


## Day 3 Tasks – Python
## ===========================


## 1. Aap supermarket gaye ho. Ek item ki price price = 120 hai. Agar price 100 se zyada ho to "Expensive" print karo, warna "Affordable".

```python
price = 120
if(price > 100):
    print("Expensive")
else:
    print("Affordable")
```

## -----------------------------


## 2. Ek student ka percentage = 40 hai. Agar 85 ya zyada hai to "Excellent", agar 60–84 ke beech hai to "Good", warna "Needs Improvement".

```python
student_percentage = 50
if(student_percentage >= 85):
    print("Excellent")
elif(student_percentage >= 60 and student_percentage < 85):
    print("Good")
else:
    print("Needs Improvement")
```

## -------------------------------------------------------


## 3. Ek company internship me agar applicant ka cgpa = 3.2 hai aur 3.0 se kam hai to "Not Eligible", warna "Eligible".

```python
applicant_cgpa = 3
if(applicant_cgpa < 3.0):
    print("Not Eligible")
else:
    print("Eligible")
```

## -------------------------


## 4. Ek grading system me percentage = 73 hai. Agar 85 ya zyada → "Excellent"  Agar 60–84 → "Good"  Agar 40–59 → "Average"  Warna → "Fail"

```python
percentage = int(input("Enter your percentage: "))
if(percentage >= 85):
    print("Excellent")
elif(percentage >= 60 and percentage < 85):
    print("Good")
elif(percentage >= 40 and percentage < 60):
    print("Average")
else:
    print("Fail")
```

## -----------------------------------------------------


## 5. Ek online shopping me bill = 3500 hai.  Agar 5000 ya zyada → "Gold Member Discount" Agar 3000–4999 → "Silver Member Discount" Agar 1000–2999 → "Basic Member Discount" Warna → "No Discount"

```python
bill  = int(input("Enter your bill: "))
if(bill >= 5000):
    print("Gold Member Discount")
elif(bill >= 3000 and bill < 5000):
    print("Silver Member Discount")
elif(bill >= 1000 and bill < 3000):
    print("Basic Member Discount")
else:
    print("No Discount")

```
## -----------------------------------------------------


## 6. Coffee Machine
### Ek coffee machine me option choose karna hai:
### Agar choice = 1 → "Espresso"
### Agar choice = 2 → "Cappuccino"
### Agar choice = 3 → "Latte"
### Warna → "Invalid Selection"

``` python
choice = int(input("Enter Choice (1 ,2 ,3) "))
if(choice == 1):
    print("Espresso")
elif(choice == 2):
    print("Cappuccino")
elif(choice == 3):
    print("Latte")
else:
    print("Invalid Selection")
```

## -------------------------


## 7. Weather Advisory
### temperature = 12 hai.
### Agar temp < 10 → "Too Cold – Wear Jacket"
### Agar 10–25 → "Pleasant Weather"
### Agar 26–35 → "Warm Day"
### Agar > 35 → "Heat Alert"

``` python
tem = int(input("Enter Temperature::> "))
if(tem < 10):
    print("Too Cold – Wear Jacket")
elif(tem >= 10 and tem <= 25):
    print("Pleasant Weather")
elif(tem >= 26 and tem <= 35):
    print("Warm Day")
elif(tem > 35):
    print("Heat Alert")
```

## -------------------------


## 8. Mobile Battery Status
### battery = 18 % hai.
### Agar ≥ 80 → "Battery Full"
### Agar 50–79 → "Battery Sufficient"
### Agar 20–49 → "Battery Low"
### Agar < 20 → "Connect Charger Immediately"

```python
battery = int(input("Enter you mobile battery charging::> "))
if(battery >= 80):
    print("Battery Full")
elif(battery >= 50 and battery < 80):
    print("Battery Sufficient")
elif(battery >= 20 and battery < 50):
    print("Battery Low")
elif(battery < 20):
    print("Connect Charger Immediately")
```


## Day 4 Tasks – Python
## ===================================

## 1. Print 1 to 10 numbers
```python
for a in range(1,11):
    print(a)
```

## 2. ⁠print even numbers 2-20

```python
for a in range(2,21):
    if(a%2==0):  
        print(a)
```

## 3. ⁠Square numbers 1-25

```python
for a in range(1, 26):
    print(f"The square of {a} is {a**2}")
```
## 4. ⁠print odd numbers 1-100

```python
for a in range(1,100):
    if(a%2!=0):  
        print(a)
```

## 5. ⁠print 1-10 with hello (eg 1 hello)
```python
for a in range(1, 11):
    print(a ,"hello")
```