from compare_result import CompareResult


class UserInterface:
    def input_number(self, min_number: int, max_number: int) -> int:
        while (True):
            input_str = input(f"\nEntrez un nombre entre {
                              min_number} et {max_number}\n")
            try:
                input_number = int(input_str)
                if (min_number <= input_number <= max_number):
                    return input_number
                else:
                    print(f"Le nombre doit être entre {
                          min_number} et {max_number}\n")
            except ValueError:
                print("Entrez un nombre entier\n")

    def output_hint(self, position_hint: CompareResult) -> None:
        if position_hint == CompareResult.MORE:
            print("Choisissez un chiffre plus grand")
        elif position_hint == CompareResult.LESS:
            print("Choisissez un chiffre plus petit")
        elif position_hint == CompareResult.EQUAL:
            print("Vous avez trouvé le bon chiffre")
        else:
            raise Exception(f"Invalid Comparer Result: {position_hint}")

    def output_result(self, nb_guess: int) -> None:
        print(f"Nombre deviné au bout de {nb_guess} essais")
