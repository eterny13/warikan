-- haskell version
data Member = NormalMember | LargeMember | SmallMember deriving (Eq, Show)

type Npeople = Int
type Totalbill = Int

normalCalc :: Npeople -> Totalbill -> [Int]
normalCalc n tb = [ch, mb] 
  where 
    mb = tb `div` n + 1
    ch = mb * n - tb

calc :: [Member] -> Totalbill -> [Integer]
calc ms tb = [ch, mb, lmb, smb] 
  where 
    nl = length $ filter (==NormalMember) ms 
    ll = length $ filter (==LargeMember) ms 
    sl = length $ filter (==SmallMember) ms 
    n  = fromIntegral nl + fromIntegral ll * 1.5 + fromIntegral sl * 0.5 

    mb  = ceiling $ fromIntegral tb / n 
    lmb = truncate $ fromIntegral mb * 1.5 
    smb = truncate $ fromIntegral mb * 0.5  
    ch  = mb * fromIntegral nl + lmb * fromIntegral ll + smb * fromIntegral sl - fromIntegral tb 

calc10yen :: Npeople -> Totalbill -> [Int]
calc10yen n tb = [mb', lmb', smb']
  where
    mb = tb `div` n + 1
    lmb = mb * 3 `div` 2 
    smb = mb `div` 2

    mb' = if mb `mod` 10 <= 4 then tb `div` n `div` 10 * 10 else tb `div` n `div` 10 * 10 + 10
    lmb' = if lmb `mod` 10 <= 4 then lmb `div` 10 * 10 else lmb `div` 10 * 10 + 10
    smb' = if smb `mod` 10 <= 4 then smb `div` 10 * 10 else smb `div` 10 * 10 + 10

main = do
  
  let s1 = normalCalc 4 3330
  print s1
  
  let s2 = calc [NormalMember, NormalMember, LargeMember, SmallMember, SmallMember] 3330
  print s2

  let s3 = calc10yen 3 3330
  print s3
