import { Cubix, parseAndRun } from './cubix.js';

document.getElementById('runBtn').addEventListener('click', async () => {
  const code = document.getElementById('codeInput').value;
  const outputContent = document.getElementById('outputContent');
  const cursor = document.getElementById('cursor');

  const cubix = new Cubix(3);
  try {
    await parseAndRun(code, cubix);
    outputContent.innerText = 'Execution complete.';
  } catch (err) {
    outputContent.innerText = `Error: ${err.message}`;
  }
});