Shader "Custom/ColorNegativ2"
{
    Properties
    {
        _MainTex ("Texture", 2D) = "white" {}
		_Color ("Color", Color) = (0,0,0,1)
    }
    SubShader
    {
		Tags { "RenderType"="Opaque" }

        Pass
        {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "UnityCG.cginc"
			
			fixed4 _Color;

            struct appdata
            {
                float4 vertex : POSITION;
                float2 uv : TEXCOORD0;
            };

            struct v2f
            {
                float2 uv : TEXCOORD0;
                float4 vertex : SV_POSITION;
            };

            sampler2D _MainTex;
            float4 _MainTex_ST;

            v2f vert (appdata v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.uv = v.uv;
                return o;
            }

            fixed4 frag (v2f i) : SV_Target
            {
                return fixed4(1 - _Color[0], 1 - _Color[1], 1 - _Color[2], 1);
            }
            ENDCG
        }
    }
}
