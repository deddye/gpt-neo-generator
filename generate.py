from transformers import pipeline
import os, sys

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# assign directory
directory = sys.argv[1]

# go through given directory
for (path, dirs, fnames) in os.walk(directory):
    qualified_filenames = (os.path.join(path, filename) for filename in fnames)
    for f in qualified_filenames:
    
        # use only files that have "prompt" in filename
        if (f.find("prompt") > 0):
            file = open(f, "r")
            while True:
                try:
                    line = file.readline()
                except:
                    print("skipping this line bc encode error")
                else:
                    prompt = line[5:]
                    
                    # generate 10 samples per prompt
                    for x in range (0,10):
                    
                        gen_output = generator(prompt, do_sample=True, min_length=200)
                        text = gen_output[0]["generated_text"]
                        output_file = open("generated_text.txt", "a")
                        output_file.write(text + "\n\n")
                        output_file.close()

                if not line:
                    file.close()
                    break

