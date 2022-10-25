import File
import String

current_module = __ENV__.file |> split("/") |> List.last()
current_number = current_module |> split(".") |> List.first()
next_number = current_number |> String.to_integer() |> Kernel.+(1) |> Integer.to_string()
new_filename = next_number <> ".exs"
rename(current_module, new_filename)
