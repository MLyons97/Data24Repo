
import ExampleClass as EC

counter_a = EC.CounterA()
counter_b = EC.CounterB()

counter_a.increment()
counter_b.increment()

counter_a.increment()
counter_b.increment()

counter_a.increment()
counter_b.increment()

counter_a.current = -10
counter_b.__current = -10

print(f"Counter A's value is {counter_a.value()}")
print(f"Counter B however is on {counter_b.value()}")

