



local _, ruta_script = reaper.get_action_context()
local carpeta_script = ruta_script:match("(.*[/\\])") 

local python_exe = "python"
local script_python = carpeta_script .. "generador_matriz.py"

-- Verificamos si hay un ítem seleccionado en la pista activa.
local item = reaper.GetSelectedMediaItem(0, 0)
if not item then
    reaper.MB("Por favor, selecciona un ítem MIDI de melodía original.", "Error", 0)
    return
end


-- INPUT DEL USUARIO
local retval, user_inputs = reaper.GetUserInputs("Tintinnabuli Parameters", 3, 
    "Base Note (ex: C), Semitones (ex: 0-4-7), T-Voice", 
    ",,")

if not retval then return end

-- Calcula cualquier bloque continuo de texto que no tenga comas, y lo asigna a las variables nota_base, intervalos y nivel respectivamente.
-- Si el usuario no ingresa nada, se asignará una cadena vacía.
local nota_base, intervalos, nivel = user_inputs:match("([^,]+),([^,]+),([^,]+)")

local archivo_MIDI = "None"
if nota_base == "a" then
    local take = reaper.GetActiveTake(item)
    local fuente = reaper.GetMediaItemTake_Source(take)
    archivo_MIDI = reaper.GetMediaSourceFileName(fuente, "")
end
-- Preparamos la instrucción exacta que se va a enviar a la consola
local cmd = string.format('cmd /c %s "%s" "%s" "%s" %s "%s" 2>&1', python_exe, script_python, nota_base, intervalos, nivel, archivo_MIDI)
-- Abrimos un proceso para ejecutar el comando y capturamos la salida estandar de Python
local gestion = io.popen(cmd)
-- Leemos toda la salida de Python (el JSON) y lo guardamos en una variable
local json = gestion:read("*a")
gestion:close()

-- Si no hubiese salida de Python, mostramos un mensaje de error y salimos del script.
if not json or json == "" then
    reaper.MB("Error: El script de Python no devolvió ningún dato.", "Error de Ejecución", 0)
    return
end

-- PARSER DE LA MATRIZ 
local function parser_matriz(json_str)
    local matriz = {}
    -- gmatch busca las lineas del JSON cuya clave y valor sean números
    for clave, valor in json_str:gmatch('"(%d+)"%s*:%s*(%d+)') do
        matriz[tonumber(clave)] = tonumber(valor)
    end
    return matriz
end

local matriz_tintinnabuli = parser_matriz(json)


-- Creamos la pista nueva al final del proyecto y la nombramos.
local num_pistas = reaper.CountTracks(0)
reaper.InsertTrackAtIndex(num_pistas, true) -- true para mantener default envelopes y FX.
local nueva_pista = reaper.GetTrack(0, num_pistas) --Seleccionamos la pista recién creada
reaper.SetOnlyTrackSelected(nueva_pista) -- Nos aseguramos de que solo esté seleccionada la nueva pista
reaper.GetSetMediaTrackInfo_String(nueva_pista, "P_NAME", "T-Voice " .. nivel, true) --Asignamos a la nueva pista el nombre


-- Creamos un nuevo ítem con las mismas coordenadas de inicio y fin que el original.
local item_pos = reaper.GetMediaItemInfo_Value(item, "D_POSITION") --Obtenemos la posición del ítem en segundos
local item_len = reaper.GetMediaItemInfo_Value(item, "D_LENGTH") --Obtenemos la longitud del ítem en segundos
local nuevo_item = reaper.CreateNewMIDIItemInProj(nueva_pista, item_pos, item_pos + item_len) --Creamos un item MIDI del mismo tamaño

--Tomamos cada item MIDI y contamos el número de eventos MIDI que tiene el ítem original.
local take_origen = reaper.GetActiveTake(item)
local take_destino = reaper.GetActiveTake(nuevo_item)
local _, num_notas = reaper.MIDI_CountEvts(take_origen) 

reaper.PreventUIRefresh(1) --Desactivamos la interfaz mientras insertamos las notas

for i = 0, num_notas - 1 do
    local _, sel, mut, start_ppq, end_ppq, chan, pitch_origen, vel = reaper.MIDI_GetNote(take_origen, i)
    
    local pitch_destino = matriz_tintinnabuli[pitch_origen]
    
    if pitch_destino and pitch_destino >= 0 and pitch_destino <= 127 then
        reaper.MIDI_InsertNote(take_destino, sel, mut, start_ppq, end_ppq, chan, pitch_destino, vel, false)
    end
end

reaper.MIDI_Sort(take_destino) -- Ordena internamente los eventos MIDI
reaper.PreventUIRefresh(-1)    -- Reactivamos la interfaz
reaper.UpdateArrange()         -- Refrescamos la vista de Reaper