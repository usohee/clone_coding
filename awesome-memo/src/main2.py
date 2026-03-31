from pymongo import MongoClient

# MongoDB 연결
client = MongoClient("mongodb://{몽고DB서버주소}")
# 데이터베이스 선택 (여기서는 'memo_db'라는 데이터베이스를 사용)
db = client["memo_db"]
# 컬렉션 선택 (여기서는 'memos'라는 컬렉션을 사용)
collection = db["memos"]

# 메모 생성 (Create)
def create_memo(title: str, content: str):
    memo = {
        "title": title,
        "content": content
    }
    result = collection.insert_one(memo)
    print(f"Inserted memo with id {result.inserted_id}")

# 메모 조회 (Read)
def read_memos():
    memos = collection.find()
    for memo in memos:
        print(memo)

# 메모 수정 (Update)
def update_memo(memo_id, title: str, content: str):
    collection.update_one(
        {"_id": memo_id},
        {"$set": {"title": title, "content": content}}
    )
    print(f"Updated memo with id {memo_id}")

# 메모 삭제 (Delete)
def delete_memo(memo_id):
    collection.delete_one({"_id": memo_id})
    print(f"Deleted memo with id {memo_id}")

​
