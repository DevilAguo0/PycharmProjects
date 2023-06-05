const FingerprintGenerator = require('fingerprint-generator');
let fingerprintGenerator = new FingerprintGenerator({
    browsers: [
        { name: "firefox", minVersion: 80 },
        { name: "chrome", minVersion: 87 },
        "safari"
    ],
    devices: [
        "desktop"
    ],
    operatingSystems: [
        "windows"
    ]
});

let { fingerprint, headers } = fingerprintGenerator.getFingerprint({
    operatingSystems: [
        "linux"
    ],
    locales: ["en-US", "en"]
});
console.log(fingerprint)
