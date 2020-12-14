travel :: [[Char]] -> (Int, Int) -> (Int, Int) -> Int
travel [] pos step = 0
travel (row:forest) pos step =
  if snd pos `mod` snd step == 0
    then travel forest ((fst pos + fst step) `mod` (length row), snd pos + 1) step
      + if row !! fst pos == '#' then 1 else 0
    else travel forest (fst pos, snd pos + 1) step

multiplyResults :: [[Char]] -> [(Int, Int)] -> Int
multiplyResults forest steps = foldl addPath 1 steps
  where addPath acc x = acc * travel forest (0, 0) x

main :: IO ()
main = do
  str <- readFile "day3/input.txt"
  print $ travel (lines str) (0, 0) (3, 1)
  print $ multiplyResults (lines str) [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
