def shuffle(arr)
    for n in 0..4
	targ = shuffle(n)
	end
end
def pairs(a, b)
    a << b
    shuffle(b)
end
shuffle(1)
pairs(1,2)

