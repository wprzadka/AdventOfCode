main :: IO ()
main = do
  input <- map read.lines <$> readFile "day10/input.txt"
  print $ (\(x, y) -> x * y) $ count $ diffs $ qsort input

diffs :: [Int] -> [Int]
diffs [x,y] = [y - x]
diffs (x:y:xs) = (y-x) : (diffs (y:xs))

count :: [Int] -> (Int, Int)
count list = foldl addNext (1, 1) list
  where
    addNext acc x
      | x == 1 = (fst acc + 1, snd acc)
      | x == 3 = (fst acc, snd acc + 1)
      | otherwise = (fst acc, snd acc)

qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort [x] = [x]
qsort (x:xs) =
  qsort(filter (\d -> d < x) xs)
  ++ [x]
  ++ qsort(filter (\d -> d > x) xs)
