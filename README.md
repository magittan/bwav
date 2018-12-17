# bwav

HackMIT Project with Brian, William, Alex, Vincent

### Inspiration

What if we could change how an average college student listened in lecture? We've all been there–those long lectures with professors that seem to drone on and on. Instead of taking messy and incomplete notes, what if a webapp could do that for you?

Luckily, speech to text APIs and machine learning are able to help make that happen. Later, we realized that this can be applied to more than just lectures–a summarized version of speeches, talks, even conference calls can boost productivity and allow for better recall and review. Our team plans to use it to aid our studying strategies for classes!

### What it does

Briefly takes in audio files, and converts the speech into text using the Rev.ai API. Afterwards, the text is fed into a summarizer API that condenses the text into a few sentences by finding the keywords used the in text and ranking the sentences that are used.

### How I built it

For the graphic aspect: we wanted it to be a simple and user friendly interface for the user. We used PHP to design a minimalistic webpage to allow users to upload files to our webapp. Using Rev.ai, we were able to process the text that was spoken and transfer that to the summarizer API. We specifically chose a summarizer that used machine learning principles to have more accurate summarizing with more flexibility of use. Lastly, outputs are indexed so they can be recalled instantly with the same file.

### Challenges I ran into

We originally designed the webpage using Flask, but later changed to PHP in order to accomodate a more flexible backend for our program. While using the speech to text API, Rev.ai generated very large amounts of data that was difficult to work with. Also, requests to Rev.ai took a lot of time to process, leading us to include our indexing feature.

### Accomplishments that I'm proud of

We made it work! The page also looks pretty! We were also able to index the speech to text summary files in order to speed up recall.

### What I learned

Curl requests and PHP are very bothersome. HackMIT is also one member’s first hackathon!

### What's next for Briefly

We discussed the possibility of using the same API’s to analyze videos and applying a sentiment analysis to determine social sentiment for use in financial situations. Specifically for Briefly, we are also thinking of including a database to store lecture summaries to be shared publicly.
