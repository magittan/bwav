import sys
import RevSpeech
import summarizer

def main():
    target = "https://support.rev.com/hc/en-us/article_attachments/200043975/FTC_Sample_1_-_Single.mp3"
    # Testing with URL
    s2t = RevSpeech.Speech2Text()
    responseString = s2t.test_workflow_with_url(target)

    # Testing with file upload
    # file = "test.mp3"
    # test_workflow_with_file(file)

    s = summarizer.Summarizer()
    responseString = s.get_summary(responseString)

    print(responseString)


if __name__ == "__main__":
    main()