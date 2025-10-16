#!/usr/bin/env bash
set -Eeuo pipefail
IFS=$'\n\t'

FRAMEWORK_DIR="${1:-}"; INPUT="${2:-}"; OUTPUT="${3:-}"; APP_DIR="${4:-}"

echo "[run.sh] FRAMEWORK_DIR=$FRAMEWORK_DIR"
echo "[run.sh] INPUT=$INPUT"
echo "[run.sh] OUTPUT=$OUTPUT"
echo "[run.sh] APP_DIR=$APP_DIR"
which python || true
python --version || true

# 2 = input inexistent
if [[ -z "${INPUT}" || ! -f "${INPUT}" ]]; then
  echo "[run.sh][ERROR] Input file not found: ${INPUT}" >&2
  ls -l "$(dirname "${INPUT:-.}")" || true
  exit 2
fi

PY="$FRAMEWORK_DIR/code/main.py"
CKPT="../$FRAMEWORK_DIR/checkpoints/macaw_chembl_trained.joblib"   # ajusta si no uses checkpoint

# 3 = script/checkpoint no trobats
if [[ ! -f "$PY" ]]; then
  echo "[run.sh][ERROR] Missing script: $PY" >&2
  exit 3
fi
if [[ ! -f "$CKPT" ]]; then
  echo "[run.sh][WARN] Checkpoint not found (continuing without it?): $CKPT" >&2
  # si és obligatori, fes `exit 3`
fi

# staging: evitem carreres amb /tmp externs
WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT
cp "$INPUT" "$WORKDIR/input.csv"
mkdir -p "$(dirname "$OUTPUT")"

echo "[run.sh] head INPUT:"
head -n 5 "$WORKDIR/input.csv" || true

set -x
# Passa el checkpoint a main.py si el fas servir
python -u "$PY" "$WORKDIR/input.csv" "$OUTPUT" || { rc=$?; echo "[run.sh][ERROR] Python failed rc=$rc" >&2; exit 4; }
set +x

echo "[run.sh] Done → $OUTPUT"
