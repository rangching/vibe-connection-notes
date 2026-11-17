// ============================================================
//  影片連結（由 site_writeback.py 自動回寫，也可以手動改）
//  youtube ：影片 ID 或網址      short  ：直式重點版（Shorts）ID
//  duration：片長 "6:35"          sections：各小節開始秒數（數量＝小節數），null 用 content.js 預估
//  noVoice ：無旁白版 ID          mp4    ：自架 MP4（沒有 YouTube 時才用）
// ============================================================

window.SERIES_PLAYLIST = ""; // 系列播放清單網址（公開或不公開後才填）
window.SERIES_TRAILER = "";  // 系列前導片 ID（延續型系列）

window.VIDEO_LINKS = {
  u01: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u02: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u03: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u04: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u05: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u06: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u07: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u08: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u09: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u10: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u11: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" },
  u12: { youtube: "", mp4: "", duration: "", sections: null, noVoice: "", short: "" }
};
