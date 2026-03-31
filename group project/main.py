from collections import deque

# Queue for posts
review_queue = deque()

# Stack for history
audit_log = []

print("Queue and Stack initialized")

# Submit post
def submit_post(post_id, content):
    post = {"id": post_id, "content": content}
    review_queue.append(post)
    print("Post submitted")

# Review post
def review_post():
    if not review_queue:
        print("No posts to review")
        return

    post = review_queue.popleft()
    print("Reviewing:", post)

    choice = input("Approve (a) or Reject (r): ")

    if choice == 'a':
        print("Approved")
    else:
        print("Rejected")

    audit_log.append(post)

# Undo review
def undo_review():
    if not audit_log:
        print("Nothing to undo")
        return

    last = audit_log.pop()
    review_queue.appendleft(last)
    print("Undo successful")

# Show queue
def show_queue():
    if not review_queue:
        print("Queue is empty")
        return

    print("\nPosts in queue:")
    for post in review_queue:
        print(post)

# MAIN PROGRAM
if __name__ == "__main__":
    while True:
        print("\n--- Moderation System ---")
        print("1. Submit Post")
        print("2. Review Post")
        print("3. Undo Review")
        print("4. View Queue")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            post_id = int(input("Enter ID: "))
            content = input("Enter content: ")
            submit_post(post_id, content)

        elif choice == '2':
            review_post()

        elif choice == '3':
            undo_review()

        elif choice == '4':
            show_queue()

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice")
    