from typing import Callable, List, Tuple, Dict

Decorator = Callable


def get_list_of_kwargs_for_function(
    identifiers: str, values: List[Tuple[str, str]]
) -> List[Dict[str, str]]:
    print(f"getting list of kwargs for function, \n{identifiers=}, {values=}")
    parse_identifiers = identifiers.split(",")
    list_of_kwargs_for_function = []
    for tuple_values in values:
        kwargs_for_function = {}
        for i, keyword in enumerate(parse_identifiers):
            kwargs_for_function[keyword] = tuple_values[i]
        list_of_kwargs_for_function.append(kwargs_for_function)

    print(f"{list_of_kwargs_for_function=}")
    return list_of_kwargs_for_function


def my_parametrize(identifiers: str, values: List[Tuple[int, int]]) -> Callable:
    def my_parametrize_decorator(function: Callable) -> Callable:
        def run_func_parametrized() -> None:
            list_of_kwargs_for_function = get_list_of_kwargs_for_function(
                identifiers=identifiers, values=values
            )
            for kwargs_for_function in list_of_kwargs_for_function:
                print(
                    f"calling function {function.__name__} with {kwargs_for_function=}"
                )
                function(**kwargs_for_function)

        return run_func_parametrized

    return my_parametrize_decorator
