import sqlite3

conn = sqlite3.connect('utube_manager.db')
cursor = conn.cursor()

cursor.execute(''' 
        Create table if not exists videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            TIME TEXT NOT NULL
        )
               
               
            ''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO VIDEOS(name, time)VALUES(?, ?)", (name, time))
    conn.commit()


def update_video(video_id, new_name, time):
    cursor.execute(
        "Update videos SET name = ?, time = ? WHERE id = ?", (new_name, time, video_id))
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()


def main():
    while True:

        print("\n Youtube manager app with db ")
        print("1 List videos")
        print("2 Add videos")
        print("3 Update videos")
        print("4 Delete videos")
        print("5 exit app")
        choice = input("Enter your choice:")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name:")
            time = input("Enter the video time:")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video ID to update")
            name = input("Enter the video name:")
            time = input("Enter the video time:")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter the video ID to delete:")
            delete_video(video_id)
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()


if __name__ == "__main__":
    main()
