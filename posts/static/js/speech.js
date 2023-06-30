let input;
let transcript;
let voiceSelect;
let voices;
let text = "";

const synth = window.speechSynthesis;

const init = () => {
  input = document.getElementById("ttsinput");
  transcript = document.getElementById("transcript");
  voiceSelect = document.getElementById("voiceselect");
  initVoices();
  synth.addEventListener("voiceschanged", (event) => {initVoices();});
  // input.addEventListener("keyUp", (event) => {
  //   if (event.key === " ") {
  //     event.preventDefault();
  //     talk();
  //   }
  // });
  input.addEventListener("keyup", (e) => {
      setTimeout(() => {
        if (input.value.includes(" ")) {
          talk();
        }
      }, 5);
  });
};

const talk = () => {
  text = input.value.trim();
  transcript.innerHTML += ` ${text}`;
  input.value = "";

  const voice = getVoiceByName(voiceSelect.selectedOptions[0].getAttribute("data-name"));

  speak(text, voice);
}

const getVoiceByName = (name) => {
  return voices.find((voice) => voice.name === name);
};

let initVoicesLock = false;

const initVoices = () => {
  if (initVoicesLock) return;
  initVoicesLock = true;
  voices = synth.getVoices();
  voiceSelect.innerHTML = "";
  voices.forEach((voice) => {
    let option = document.createElement("option");
    option.textContent = `${voice.name} (${voice.lang})`;
    option.setAttribute("data-lang", voice.lang);
    option.setAttribute("data-name", voice.name);
    voiceSelect.appendChild(option);
  });
  initVoicesLock = false;
}

const speak = (text, voice) => {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.rate = 1;
  utterance.pitch = 1;
  utterance.voice = synth.getVoices()[0];
  utterance.volume = 1;
  utterance.voice = voice;

  utterance.onend = (event) => {
    console.log("SpeechSynthesisUtterance.onend");
  };

  utterance.onerror = (event) => {
    console.error("SpeechSynthesisUtterance.onerror");
  }

  console.log(text);

  synth.speak(utterance);
};

window.addEventListener("load", () => {
  init();
});
