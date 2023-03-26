from transformers import pipeline
import os, sys

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# assign directory
directory = sys.argv[1]

for (path, dirs, fnames) in os.walk(directory):
    qualified_filenames = (os.path.join(path, filename) for filename in fnames)
    for f in qualified_filenames:
        if (f.find("prompt") > 0):
            file = open(f, "r")
            while True:
                try:
                    line = file.readline()
                except:
                    print("skipping this line bc encode error")
                else:
                    prompt = ""
                    if (len(line) > 45):
                        prompt = line[5:45]
                    else: 
                        prompt = line[5:]
                    for x in range (0,10):
                        gen_output = generator(prompt, do_sample=True, min_length=2000)
                        text = gen_output[0]["generated_text"]

                        output_file = open("generated_text.txt", "a")
                        output_file.write(text)
                        output_file.write("\n\n")
                        output_file.close()

                if not line:
                    file.close()
                    break

