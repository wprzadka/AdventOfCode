import Data.List

extractAll :: [[Char]] -> [([Char], [Char])]
extractAll [x] = [extractRowAndSeat x]
extractAll (x:xs) = extractRowAndSeat x : extractAll xs

extractRowAndSeat :: [Char] -> ([Char], [Char])
extractRowAndSeat word = foldr addElem ("", "") word
  where addElem x acc = if x == 'F' || x == 'B' then (x : fst acc, snd acc) else (fst acc, x : snd acc)

getRow :: String -> Int
getRow x = fst $ getInterval 'F' x (0, 127)

getSeat :: String -> Int
getSeat x = fst $ getInterval 'L' x (0, 7)

getInterval :: Char -> String -> (Int, Int) -> (Int, Int)
getInterval chr [] (lower, upper) = (lower, upper)
getInterval chr (x:xs) (lower, upper)
  | x == chr = getInterval chr xs (lower, (lower + upper) `div` 2)
  | otherwise = getInterval chr xs ((lower + upper) `div` 2 + 1, upper)

multAll :: [([Char], [Char])] -> [Int]
multAll [] = []
multAll [x] = [(getRow (fst x)) * 8 + (getSeat (snd x))]
multAll (x:xs) = idNum x : multAll xs
  where
    idNum x = (getRow (fst x)) * 8 + (getSeat (snd x))

findMissing :: [Int] -> Int
findMissing [z] = -1
findMissing (x:z:xs) = if x + 1 == z then findMissing (z:xs) else x + 1

main :: IO ()
main = do
  str <- readFile "day5/input.txt"
  let input = extractAll $ lines str
  print $ maximum (multAll input)
  print $ findMissing (sort (multAll input))
