from src.main.model.SortType import SortType
from src.main.model.ruler import Ruler
from src.main.model.brand import Brand
from src.main.model.colour import Colour


class OfficeToolManagerUtils:

    @staticmethod
    def sort_by_price_in_uah(input_tool_list, input_sort_type):
        """
        Testing sorter by price in UAH
        >>> test_ruler1 = Ruler(None,110,brand=Brand(1),colour=Colour(1),0, 20,0,0)
        >>> test_ruler2 = Ruler(None,200,brand = Brand(1),colour=Colour(1),0,30)
        >>> test_ruler3 = Ruler(None,80,brand = Brand(1),colour=Colour(1),0,10)
        >>> test_ruler_list = [test_ruler1,test_ruler2,test_ruler3]
        >>> OfficeToolManagerUtils.sort_by_price_in_uah(test_ruler_list, SortType(1))
        >>> print(test_ruler_list[0].price_in_uah)
        80
        >>> print(test_ruler_list[2].price_in_uah)
        200
        """
        if input_sort_type == SortType(1):
            input_tool_list.sort(key=lambda tool_to_sort: tool_to_sort.price_in_uah)
        elif input_sort_type == SortType(2):
            input_tool_list.sort(key=lambda tool_to_sort: tool_to_sort.price_in_uah, reverse=True)
        else:
            print("cant be sorted by price in uah")

    @staticmethod
    def sort_by_weight_in_grams(input_tool_list, input_sort_type):
        """
        Testing sorter by weight in grams
        >>> test_ruler_list = [Ruler(None,110,0,20),Ruler(None,200,0,30),Ruler(None,80,0,10)]
        >>> OfficeToolManagerUtils.sort_by_weight_in_grams(test_ruler_list, SortType(2))
        >>> print(test_ruler_list[0].weight_in_grams)
        30
        >>> print(test_ruler_list[2].weight_in_grams)
        10
        """
        if input_sort_type == SortType(1):
            input_tool_list.sort(key=lambda tool_to_sort: tool_to_sort.weight_in_grams)
        elif input_sort_type == SortType(2):
            input_tool_list.sort(key=lambda tool_to_sort: tool_to_sort.weight_in_grams, reverse=True)
        else:
            print("cant be sorted by weight in grams")


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
