defmodule Solution do
  @spec longest_common_prefix(strs :: [String.t]) :: String.t
  def longest_common_prefix([]), do: ""

  def longest_common_prefix(strs) do
    Enum.reduce(strs, hd(strs), fn str, acc ->
      common_prefix(acc, str)
    end)
  end

  defp common_prefix(a, b) do
    a_chars = String.graphemes(a)
    b_chars = String.graphemes(b)

    a_chars
    |> Enum.zip(b_chars)
    |> Enum.take_while(fn {c1, c2} -> c1 == c2 end)
    |> Enum.map(fn {c, _} -> c end)
    |> Enum.join()
  end
end