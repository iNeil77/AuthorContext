 local file = io.open("/home/soham/IRE/context10000.txt", "r");
 local arr = {}
 for line in file:lines() do
    table.insert (arr, line);
 end
 io.close(file)

 print((arr[1]))
 print(table.getn(arr))

 function mysplit(inputstr, sep)
        if sep == nil then
                sep = "%s"
        end
        local t={} ; i=1
        for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
                t[i] = str
                i = i + 1
        end
        return t
 end


 --[[
--------------------------------------------
Skip-gram with negative sampling (Skip-Gram)
--------------------------------------------
References:
1. http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf
2. http://cs224d.stanford.edu/lecture_notes/LectureNotes1.pdf
]]--

require 'torch'
require 'nn'
require 'lightningmdb'

-- Define your vocabulary map
-- Define constants
vocab_size = 10000 -- number of words in the vocabulary
word_embed_size = 100 -- size of word embedding you are looking for
learning_rate = 0.01 -- initial learning rate for the training
window_size = 1-- no. of surrounding words to predict. 2 means left and right word
max_epochs = 50 -- number of complete passes of the training set
neg_samples_per_pos_word = 1 -- no of negative context for every positive (word, context) pair
dataset={}
label_1 = torch.Tensor({1, 0}) -- 0 denotes negative samples; 1 denotes the positve pairs

-- Prepare your dataset
for i=1,9267 do
    temp={}
	temp= mysplit(arr[i],',')
	word_1 = torch.Tensor{tonumber(temp[1])}
	context_1 = torch.Tensor{tonumber(temp[2]), tonumber(temp[3])} -- P(i, nlp | like) (Note: 'dl' is a sample negative context for 'like')
	dataset[i] = {{context_1, word_1}, label_1}
end
print(arr[2])
function dataset:size() return 9267 end -- define the number of input samples in your dataset (which is 2)
print("Initiakizing look up and Modues..")
-- Define your model
word_lookup = nn.LookupTable(vocab_size, word_embed_size)
context_lookup = nn.LookupTable(vocab_size, word_embed_size)
model = nn.Sequential()
model:add(nn.ParallelTable()) -- when the input is a table of tensors (context and word), we need parallel table.
model.modules[1]:add(context_lookup) -- consumes context word indices, stacks the context embeddings in a matrix and outputs it.
model.modules[1]:add(word_lookup) -- consumes target word index, and outputs the embedding.
model:add(nn.MM(false, true)) -- 'true' to transpose the word embedding before matrix multiplication
model:add(nn.Sigmoid()) -- this non-linearity keeps the output between 0 and 1 (ideal for our 2-class problem)

-- Define the loss function (Binary cross entropy error)
criterion = nn.BCECriterion()
print("Done!")

-- Define the trainer
trainer = nn.StochasticGradient(model,criterion)
trainer.learningRate = learning_rate
trainer.maxIteration = max_epochs

print('Word Lookup before learning')
--weight_initial=word_lookup.weight
-- print(word_lookup.weight)

-- Train the model with dataset
trainer:train(dataset)

-- Get the word embeddings
print('\nWord Lookup after learning')
--weight_final=word_lookup.weight

-- print(word_lookup.weight)
local file=io.open('weight60000.txt','w')
s1=''
for i=1,10000 do
    for j=1,100 do
        s1=(s1 .. tostring(word_lookup.weight[i][j]) .. ' ')
    end
    s1=s1 .. '\n'
    file:write(s1)
    s1=''
end
io.close(file)