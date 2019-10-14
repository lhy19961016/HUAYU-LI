# HUAYU-LI
Homework 5cem on ЭВМ
I used testing database of VoxCeleb2(about 2.4GB,40000 sound-files，
Because of the computing power of the computer, I sliced all the files and sliced them to 1000.)


Time used：


Common program:136.81291890144348 sec


5 Multithreads program:66.83121180534363 sec


5 Multiproccesses program:64.87572836875916 sec



TAP:Why is multithreading slower?
The reason is GIL. In the CPython interpreter (the mainstream interpreter for the Python language), there is a Global Interpreter Lock. When the interpreter interprets the Python code, you need to get the lock first, meaning that any At that time, only one thread may execute the code. If other threads want to obtain the CPU to execute the code instruction, they must first obtain the lock. If the lock is occupied by other threads, the thread can only wait until the thread that owns the lock. It is only possible to release the lock to execute the code instruction.
