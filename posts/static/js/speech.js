let input;
let transcript;
let voiceSelect;
let specialChars;
let voices;
let saveButton;
let text = "";

const synth = window.speechSynthesis;

const init = () => {
  input = document.getElementById("ttsinput");
  transcript = document.getElementById("transcript");
  voiceSelect = document.getElementById("voiceselect");
  specialChars = document.getElementById("specialChars");
  saveButton = document.getElementById("save");
  specialChars.value = "qq";
  initVoices();
  initSave();
  synth.addEventListener("voiceschanged", (event) => {initVoices();});
  // input.addEventListener("keyUp", (event) => {
  //   if (event.key === " ") {
  //     event.preventDefault();
  //     talk();
  //   }
  // });
  input.addEventListener("keyup", (e) => {
      setTimeout(() => {
          if (input.value.includes(specialChars.value)) {
            talk();
          }
      }, 5);
  });
};

const talk = () => {
  text = input.value.trim().replace(specialChars.value, ".").trim();
  transcript.innerHTML += ` ${text}`;
  input.value = "";

  const voice = getVoiceByName(voiceSelect.selectedOptions[0].getAttribute("data-name"));

  speak(text, voice);
}

const getVoiceByName = (name) => {
  return voices.find((voice) => voice.name === name);
};

const initSave = () => {
  saveButton.addEventListener("click", (e) => {
    const selectedVoice = voiceSelect.selectedOptions.length > 0 ? voiceSelect.selectedOptions[0].getAttribute("data-name") : null;
    if (selectedVoice) {
      sessionStorage.setItem("selectedVoice", selectedVoice);
    }
  });
}

let initVoicesLock = false;

let hasSetSavedVoice = false;

const initVoices = () => {
  if (initVoicesLock) return;
  initVoicesLock = true;
  voices = synth.getVoices();
  voices.sort((a, b) => a.lang.localeCompare(b.lang));

  const selectedVoice = voiceSelect.selectedOptions.length > 0 ? voiceSelect.selectedOptions[0].getAttribute("data-name") : null;
  voiceSelect.innerHTML = "";
  voices.forEach((voice) => {
    let option = document.createElement("option");
    option.textContent = `${voice.name} (${voice.lang})`;
    option.setAttribute("data-lang", voice.lang);
    option.setAttribute("data-name", voice.name);
    if (!hasSetSavedVoice && voice.name === sessionStorage.getItem("selectedVoice")) {
      option.selected = true;
      hasSetSavedVoice = true;
    }
    else if (voice.name === selectedVoice) {
      option.selected = true;
    }
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
