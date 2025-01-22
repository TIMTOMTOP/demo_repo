from subpkg.moduleA import Child, top_level_func
from subpkg.moduleB import AnotherClass

def main():
    child = Child()
    child.child_method("test")

    ac = AnotherClass()
    ac.another_method()

    result = top_level_func(5, 10)
    print("Result from top_level_func:", result)

if __name__ == "__main__":
    main()