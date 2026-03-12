#!/usr/bin/env python3
"""Nexa Friend Finder - 好友推荐"""
import random, json

class FriendFinder:
    def __init__(self):
        self.interests = ["游戏", "音乐", "编程", "美食", "旅行", "电影"]
        self.users = [
            {"name": "Alice", "interests": ["游戏", "音乐"]},
            {"name": "Bob", "interests": ["编程", "游戏"]},
            {"name": "Carol", "interests": ["美食", "旅行"]},
        ]
    
    def find_by_interests(self, my_interests):
        matches = []
        for user in self.users:
            common = set(user["interests"]) & set(my_interests)
            if common:
                matches.append({
                    "name": user["name"],
                    "common_interests": list(common),
                    "match_score": len(common)
                })
        return sorted(matches, key=lambda x: x["match_score"], reverse=True)
    
    def get_random_suggestion(self):
        return random.choice(self.users)

if __name__ == "__main__":
    ff = FriendFinder()
    matches = ff.find_by_interests(["游戏", "编程"])
    print(json.dumps(matches, ensure_ascii=False, indent=2))
