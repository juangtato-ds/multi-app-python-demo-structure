from celery_tasks import concatenate, exponent, square_root
import time

print("Do concatenate task")
concatenate_a = concatenate.delay("Hello", "World", "!!")
concatenate_b = concatenate.delay("Hello", "World")
time.sleep(2)

if concatenate_a.ready():
    print(f"Concatenate result: {concatenate_a.get(timeout=5)}")
else:
    print("Concatenate function is not ready")

if concatenate_b.ready():
    print(f"Concatenate result: {concatenate_b.get(timeout=3)}")
else:
    print("Concatenate function is not ready")

print("Do exponent task")
exponential = exponent.delay(3)
time.sleep(2)

if exponential.ready():
    print(f"Exponent result: {exponential.get(timeout=3)}")
else:
    print("Exponent function is not ready")

print("Do square root task")
sqrt = square_root.delay(4)
time.sleep(2)

if sqrt.ready():
    print(f"Square root result: {sqrt.get(timeout=3)}")
else:
    print("Square root function is not ready")