#!/usr/bin/env python3
"""
AI Dating Assistant - Market & Competitor Research Utility
Queries Apple iTunes Search API and Google Play Store for metrics, ratings, and pricing.
"""

import urllib.request
import urllib.parse
import json
import re
import sys

def search_app_store(queries, limit=25):
    print(f"[*] Querying Apple App Store for queries: {queries}")
    apps = {}
    for q in queries:
        url = f"https://itunes.apple.com/search?term={urllib.parse.quote(q)}&entity=software&country=us&limit={limit}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                for item in data.get("results", []):
                    tid = item.get("trackId")
                    if tid not in apps:
                        apps[tid] = {
                            "name": item.get("trackName"),
                            "seller": item.get("sellerName"),
                            "rating": item.get("averageUserRating"),
                            "reviews": item.get("userRatingCount") or 0,
                            "price": item.get("formattedPrice"),
                            "genres": item.get("genres"),
                            "url": item.get("trackViewUrl")
                        }
        except Exception as e:
            print(f"Error querying {q}: {e}")
    
    sorted_apps = sorted(apps.values(), key=lambda x: x["reviews"], reverse=True)
    return sorted_apps

def fetch_play_store_apps(package_ids):
    print(f"[*] Querying Google Play Store for {len(package_ids)} packages")
    results = []
    for pkg in package_ids:
        url = f"https://play.google.com/store/apps/details?id={pkg}&hl=en&gl=US"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(req) as resp:
                html = resp.read().decode("utf-8")
                title_match = re.search(r"<title[^>]*>([^<]+)</title>", html)
                dl_match = re.search(r"<div class=\"ClM7O\">([^<]+)</div><div class=\"g1rdde\">Downloads</div>", html)
                rating_match = re.search(r"aria-label=\"Rated ([0-9\.]+) stars", html)
                reviews_match = re.search(r"<div class=\"g1rdde\">([0-9\.]+[K|M]? reviews)</div>", html)

                results.append({
                    "package": pkg,
                    "title": title_match.group(1).split(" - Apps")[0] if title_match else pkg,
                    "downloads": dl_match.group(1) if dl_match else "N/A",
                    "rating": rating_match.group(1) if rating_match else "N/A",
                    "reviews": reviews_match.group(1) if reviews_match else "N/A"
                })
        except Exception as e:
            print(f"Error querying Play Store package {pkg}: {e}")
    return results

if __name__ == "__main__":
    print("=== App Store AI Dating Assistants ===")
    app_store_results = search_app_store(["ai dating assistant", "rizz ai", "dating wingman"])
    for a in app_store_results[:15]:
        print(f"- {a['name'][:35]:35} | {str(a['rating'])[:4]}★ | {a['reviews']:6} revs | {a['seller']}")

    print("\n=== Google Play AI Dating Assistants ===")
    play_pkgs = [
        "com.clovers.rizz",
        "com.ignitiondating.wingai",
        "ai.yourmove.app",
        "ai.smoothspeak.smoothspeak",
        "ai.casanova.datingcopilot",
        "so.rizzler",
        "ai.blush"
    ]
    play_results = fetch_play_store_apps(play_pkgs)
    for p in play_results:
        print(f"- {p['title'][:30]:30} | {p['rating']}★ | {p['downloads']:8} DLs | {p['reviews']} revs")
