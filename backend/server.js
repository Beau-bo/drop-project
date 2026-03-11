const express = require("express");
const cors = require("cors");
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const app = express();
app.use(cors());
app.use(express.json());
const users = [];

app.post("/api/auth/register", async (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) return res.status(400).json({ error: "请填写用户名和密码" });
  if (users.find(u => u.username === username)) return res.status(400).json({ error: "用户名已存在" });
  const hashedPassword = await bcrypt.hash(password, 10);
  const user = { id: Date.now(), username, password: hashedPassword };
  users.push(user);
  res.json({ message: "注册成功", user: { id: user.id, username } });
});

app.post("/api/auth/login", async (req, res) => {
  const { username, password } = req.body;
  const user = users.find(u => u.username === username);
  if (!user || !await bcrypt.compare(password, user.password)) {
    return res.status(400).json({ error: "用户名或密码错误" });
  }
  const token = jwt.sign({ userId: user.id }, "secret-key");
  res.json({ message: "登录成功", token, user: { id: user.id, username } });
});

app.get("/api/projects", (req, res) => {
  res.json([{ id: 1, title: "AI 客服 SaaS 半成品", hook: "基于 GPT-4...", views: 234 }]);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log("✅ 服务器运行在 http://localhost:" + PORT));
