const express = require('express');
const os = require('os');
const app = express();

function formatUptime(seconds) {
  const days = Math.floor(seconds / (3600 * 24));
  const hrs = Math.floor((seconds % (3600 * 24)) / 3600);
  const mins = Math.floor((seconds % 3600) / 60);
  return `${days}d ${hrs}h ${mins}m`;
}

app.get('/api/stats', (req, res) => {
  const uptime = formatUptime(os.uptime());
  const totalMem = os.totalmem();
  const freeMem = os.freemem();
  const usedMem = totalMem - freeMem;

  const memUsage = `${(usedMem / 1024 / 1024).toFixed(1)}MB / ${(totalMem / 1024 / 1024).toFixed(1)}MB`;
  const cpuLoad = os.loadavg()[0].toFixed(2); // 1-min average

  res.json({
    uptime,
    cpuLoad,
    memUsage
  });
});

app.listen(3000, () => {
  console.log("Stats API running on port 3000");
});
